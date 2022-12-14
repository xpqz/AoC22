'iotag'⎕cy'dfns'
data ← ⌽¨⊃,/⊃,/{⍺,¨⍵}/¨{⊃iotag/⍵}¨¨⊃,/{2{↓⍉↑⍺⍵}/⍎¨'(\d+),(\d+)'⎕s'\1 \2'⊢⍵}¨⊃⎕nget'd/14'1
cave ← 1@data⊢1000 1000⍴0
maxy←⌈/⊣/↑data

pour ← {
    ⍺<⊃⍵:0
    0=cave[⊂⍵+1 0]:⍺∇⍵+1 0
    0=cave[⊂⍵+1 ¯1]:⍺∇⍵+1 ¯1
    0=cave[⊂⍵+1 1]:⍺∇⍵+1 1
    ⊢cave[⊂⍵]←2
}

_←{maxy pour 0 500}⍣{0=⍵}⊢1
+/2=,cave ⍝ part1

cave ← 1@data⊢1000 1000⍴0
cave[maxy+2;]←1

_←{(maxy+3) pour 0 500}⍣{0≠cave[⊂0 500]}⊢1
+/2=,cave ⍝ part2
