⎕IO←1
d←⊃⎕NGET'd/3'1⋄l←∊(⎕C⎕A)⎕A⋄f←{∪⊃∩/⍵}
+⌿l⍳∊{f↓2(2÷⍨≢⍵)⍴⍵}¨d ⍝ part 1
+⌿l⍳∊f¨↓(3÷⍨≢d)3⍴d    ⍝ part 2

