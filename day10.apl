d←'-'⎕r'¯'¨⊃⎕nget'd/10'1
cycle ← 0
X ← 1
scanline ← 241⍴0
addx ← {
    cycle +← 1
    scanline[cycle]←X
    cycle +← 1
    scanline[cycle]←X
    X+←⍵
    ⍬
}
∇ f←noop
  cycle+←1
  scanline[cycle]←X
  f←⍬
∇

_←{_←⍎¨⍵⋄⍬}⍣{cycle>220}⊢d
pos ← 20 60 100 140 180 220
+/pos×scanline[pos]

f←{v←40|¯1+40|⍵⋄((⍺[⍵]-1)≤v)∧(v≤⍺[⍵]+1):'#'⋄'.'}
6 40⍴scanline∘f¨1+⍳240