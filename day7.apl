data←⊃⎕nget'd/7'1
sizes←⍬
day7←{
    data←⍵
    1↓{
        (_ size idx) ← ⍵
        idx≥≢data: 1 size idx
        line ← idx⊃data
        n←⊃(//⎕vfi line)
        1=≢n:0 (size+⊃n) (idx+1)
        '..'(≡∨1∊⍷)line:1 size idx
        '$ cd'(≡∨1∊⍷)line: (0 (size+dir_size) (idx+1))⊣(sizes,←dir_size)⊣(dir_size idx) ← (idx+1) day7 data
        0 size (idx+1)
    }⍣{⊃⍵}⊢0 0 ⍺
}
_←0 day7 data
total←+/∊{//⎕vfi⍵}¨data
target←3e7-7e7-⊃⊖sizes
+⌿sizes/⍨sizes<100000
⌊/sizes/⍨sizes>target

