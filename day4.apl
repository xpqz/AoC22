d←⊃⎕NGET('d/4')1⋄(p1 p2)←0
_←{(a b c d)←1⊃'-,'⎕VFI⍵⋄p1+←((a≥c)∧(b≤d))∨(c≥a)∧d≤b⋄p2+←~(a>d)∨c>b}¨d
p1 p2