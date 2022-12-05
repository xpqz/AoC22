d←⊃⎕nget'd/5'1
day5←{⎕IO←1
    (st r)←(''∘≢¨⍵)⊆⍵
    st←⌽¨x/⍨''∘≢¨x←{⍵∊⎕a}{⍵/⍨⍺⍺ ⍵}¨↓⍉↑st
    _←⍺⍺{
        0=≢⍵:⍬
        (a b c) ← ⊃⍵
        cr←,(-a)↑b⊃st
        (b⊃st)←,(-a)↓b⊃st
        (c⊃st),←⍺⍺cr
        ∇1↓⍵
    } {⊃(//⎕vfi⍵)}¨r
    ∊¯1∘↑¨st
}
⌽day5 d
⊢day5 d