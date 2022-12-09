d←⍉↑' '(≠⊆⊢)¨⊃⎕nget'd/9'1
mag←⍎¨1⌷d⋄dir←'URDL'⍳∊0⌷d
moves←1 0J1 ¯1 0J¯1[dir]×mag
headpath←∊2{⍺+(-×∆)×⍳|∆←⍺-⍵}/+\0,moves
g←{1.5>||⍵-⍺:⍺⋄⍺+0j1⊥×11 9○⍵-⍺}
tailp←{a←⍬⋄0{0=≢⍵:a⋄a,←v←⍺g⊃⍵⋄v∇1↓⍵}⍵}
tailpath←tailp headpath
≢∪tailpath ⍝ part1

⍝ part2: 10-tails
paths ← ⊂headpath⋄_←{paths,←⊂p←tailp ⍵⋄p}⍣9⊢headpath
1+≢∪9⊃paths ⍝ part2
