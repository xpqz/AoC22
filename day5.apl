⎕IO←1
(st r)←{⍵⊆⍨×≢¨⍵}⊃⎕NGET'd/5'1
stacks←{⍵↓⍨-⊥⍨' '=⍵}¨↓1↓⍤1⌽⍉(↑st)[;¯2+4×⍳9]
day5←{0=≢⍵:∊¯1∘↑¨⍺⋄(a b c)←⊃⍵⋄cr←,(-a)↑b⊃s←⍺⋄(b⊃s)←,(-a)↓b⊃s⋄(c⊃s),←⍺⍺cr⋄s∇1↓⍵}
stacks ⌽day5 rules←{⊃(//⎕VFI⍵)}¨r
stacks ⊢day5 rules