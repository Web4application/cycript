type expr =

  | Var of string
  | Int of int
  | ObjCMessage of expr * expr          (* [object message] *)

  | AwaitExpr of expr                   (* await expression *)
  | AsyncFunction of string * expr list (* async function(args) { body } *)

(** Check if an 'await' is inside a synchronous Objective-C block **)
let rec is_safe_usage = function

  | AwaitExpr (ObjCMessage _) -> false (* Potential deadlock: awaiting inside a sync msg *)
  | ObjCMessage (e1, e2) -> is_safe_usage e1 && is_safe_usage e2
  | _ -> true
