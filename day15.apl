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

chkrng ← {(l r)←⊃1↑⍵⋄⍺<l:⍺⋄x←⍺⌈r+1⋄x>⍺⍺:¯1⋄x∇1↓⍵}

mr←{ ⍝ Merge potentially disjointed ranges
    h←⊃c←⊆⍵
    l←⊃⌽c
    ⍺[0] > l[1]: c,⊂⍺
    ⍺[1] > l[0]: (¯1↓c),⊂l[0] (l[1]⌈⍺[1])
    c
}

part2 ← {⍵>⍺: ⍬⋄r←¯1 (⍺ chkrng) ⊃mr/⌽ranges ⍵⋄r≠¯1: ⍵ +big r×big ⍺⋄⍺∇⍵+1}
4000000 part2 0 ⍝ part 2


