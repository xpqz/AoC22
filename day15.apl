data←{⍎¨' '(≠⊆⊢)⍵}¨'x=(-?\d+), y=(-?\d+)'⎕S'\1 \2'⊃⎕NGET'd/15'1
data←(2÷⍨≢data)2⍴data
mhd←{+⌿|-⌿↑⍺⍵}/data
sensors←⍉↑⊣/data
beacons←⍉↑⊢/data

ranges ← {
    ex ← 0<mx←mhd-|(1⌷sensors)-⍵
    l ← ex/(0⌷sensors)-mx
    r ← ex/(0⌷sensors)+mx
    {⍵[⍋⍵]}↓⍉↑l r
}

merged←⊃{(x y)←↓⍉↑⍺⍵⋄(⌊/x)(⌈/y)}/srng←ranges 2000000
bx←∪(target=1⌷beacons)/1⌷beacons
remove←+/(bx≥merged[0])∧(bx≤merged[1])

(1+|-/merged)-+/(bx≥merged[0])∧(bx≤merged[1]) ⍝ part 1



