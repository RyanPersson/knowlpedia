import Lean
import Lean.Util.FoldConsts
import Lean.Util.FindExpr

open Lean

/- Run with the readable edition's pinned toolchain and Lake search path.
   Follow the expression and inductive-block rules of LeanExport.Basic.
   Keep expression edges and kernel-generated block members distinguishable. -/
def expressionDeps (e : Expr) : NameSet := Id.run do
  let mut result := e.getUsedConstantsAsSet
  if (e.find? fun x => match x with | .lit (.natVal _) => true | _ => false).isSome then
    result := result.insert ``Nat
  if (e.find? fun x => match x with | .lit (.strVal _) => true | _ => false).isSome then
    result := (result.insert ``Char.ofNat).insert ``String.ofList
  return result

def declKind : ConstantInfo → String
  | .axiomInfo _ => "axiom"
  | .thmInfo _ => "theorem"
  | .defnInfo _ => "definition"
  | .opaqueInfo _ => "opaque"
  | .quotInfo _ => "quotient primitive"
  | .inductInfo _ => "inductive"
  | .ctorInfo _ => "constructor"
  | .recInfo _ => "recursor"

def main (args : List String) : IO Unit := do
  let mod :: roots := args | throw (IO.userError "Expected a module and one or more root declarations")
  if roots.isEmpty then throw (IO.userError "No roots supplied")
  initSearchPath (← findSysroot)
  let env ← importModules #[{ module := mod.toName }] {}
  let mut recursors : NameMap NameSet := {}
  for (_, info) in env.constants do
    if let .recInfo r := info then
      for family in r.all do
        recursors := recursors.insert family ((recursors.getD family {}).insert r.name)
  let mut todo := roots.toArray.map String.toName
  let mut visited : NameSet := {}
  let out ← IO.getStdout
  while let some name := todo.back? do
    todo := todo.pop
    if visited.contains name then continue
    visited := visited.insert name
    let some info := env.find? name | throw (IO.userError s!"Missing {name}")
    if info.isUnsafe then continue
    let mut deps := expressionDeps info.type
    if let some val := info.value? (allowOpaque := true) then
      deps := deps.union (expressionDeps val)
    let mut block : NameSet := {}
    match info with
    | .inductInfo v =>
      block := (NameSet.ofList (v.all ++ v.ctors)).union (recursors.getD name {})
    | .recInfo v =>
      block := NameSet.ofList v.all
      for rule in v.rules do deps := deps.union (expressionDeps rule.rhs)
    | .ctorInfo v => block := block.insert v.induct
    | .quotInfo _ => block := NameSet.ofList [``Eq, `Quot, ``Quot.mk, ``Quot.ind, ``Quot.lift]
    | _ => pure ()
    deps := deps.erase name
    block := (block.erase name).filter fun n => !deps.contains n
    for child in deps do todo := todo.push child
    for child in block do todo := todo.push child
    let modName := (env.getModuleIdxFor? name).map (fun i => env.header.moduleNames[i.toNat]!)
    let names (s : NameSet) := s.toList.map Name.toString
    out.putStrLn (Json.arr #[toJson name.toString, toJson (modName.map Name.toString),
      toJson (declKind info), toJson (names deps), toJson (names block)]).compress
