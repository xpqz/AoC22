SIZES←⍬
day7←{
    d←⍵
    1↓{
        (_ s i)←⍵
        i≥≢d: 1 s i
        l←i⊃d
        1=≢n←⊃(//⎕VFI l):0(s+⊃n)(i+1)
        '..'(≡∨1∊⍷)l:1 s i
        '$ cd'(≡∨1∊⍷)l: (0(s+ds)(i+1))⊣(SIZES,←ds)⊣(ds i)←(i+1)day7 d
        0 s (i+1)
    }⍣{⊃⍵}⊢0 0 ⍺
}
_←0 day7 data←⊃⎕NGET'd/7'1
+⌿SIZES/⍨SIZES<100000
⌊/SIZES/⍨SIZES>3e7-7e7-⊃⊖SIZES

