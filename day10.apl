c X ← 0 1⋄ln ← 241⍴0
addx ← {ln[c+1 2]←X⋄c+←2⋄X+←⍵⋄⍬}
∇ f←noop
  c+←1⋄ln[c]←X
  f←⍬
∇

_←{_←⍎¨⍵⋄⍬}⍣{c>220}'-'⎕r'¯'¨⊃⎕NGET'd/10'1
+/p×ln[p←20 60 100 140 180 220]
f←{v←40|¯1+40|⍵⋄((⍺[⍵]-1)≤v)∧(v≤⍺[⍵]+1):'#'⋄'.'}
6 40⍴ln∘f¨1+⍳240