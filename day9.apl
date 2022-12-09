⍝ Read data, separate into vectors for direction and magnitude
d←⍉↑' '(≠⊆⊢)¨⊃⎕nget'd/9'1 

mag←⍎¨1⌷d⋄dir←'URDL'⍳∊0⌷d

⍝ Convert to complex offsets of the magnitude in specified direction
moves←1 0J1 ¯1 0J¯1[dir]×mag 

⍝ Expand the 'gaps' -- 0 4 means 0 1 2 3 4 etc. This gives the path of
⍝ the head knot
headpath←∊2{⍺+(-×∆)×⍳|∆←⍺-⍵}/+\0,moves

⍝ Helper func: if tail is more than 1 step either vertically or horizontally,
⍝ move diagonally. If within 1 step in both, remain. Otherwise, move 1 step
⍝ towards head.
g←{1.5>|⍵-⍺:⍺⋄⍺+0j1⊥×11 9○⍵-⍺}

⍝ First tail: follow the head
tailp←{a←⍬⋄0{0=≢⍵:a⋄a,←v←⍺g⊃⍵⋄v∇1↓⍵}⍵}
tailpath←tailp headpath

≢∪tailpath ⍝ part1

⍝ part2: 10-tails -- actually rather easy: repeatedly do part1, but
⍝ with the previous tail as the new head.
paths ← ⊂headpath⋄_←{paths,←⊂p←tailp ⍵⋄p}⍣9⊢headpath

⍝ Only look at the _actual_ tail positions.
1+≢∪9⊃paths ⍝ part2
