# Dynamic Array Amortized Analysis

## Background

A dynamic array starts with an initial capacity and grows by doubling its size whenever it runs out of space. While individual insertions might require O(n) time during resizing, we can show that the amortized cost per operation is actually O(1).

## Analysis Methods

### 1. Aggregate Method Analysis

The aggregate method examines the total cost of performing n operations and divides by n to get the amortized cost per operation.

#### Resizing Pattern
- Initial capacity: 1
- Resizing occurs at insertions: 1, 2, 4, 8, 16, ..., 2ᵏ
- Where k = ⌊log₂n⌋

#### Cost Breakdown
1. **Regular Insertions**
   - Each insertion without resize: O(1)
   - Total regular insertion cost: O(n)

2. **Resize Operations**
   - At size i, copying i elements costs i operations
   - Resize costs: 1 + 2 + 4 + 8 + ... + 2ᵏ
   - This forms a geometric series
   - Sum ≤ 2n (can be proven by showing each term is half of the next)

#### Total Cost Analysis
```
Total Cost = Regular Insertions + Resize Costs
           = O(n) + O(n)
           = O(n)

Amortized Cost per Operation = O(n)/n = O(1)
```

### 2. Accounting Method Analysis

The accounting method assigns a cost to each operation that may be higher than its actual cost, saving the excess as credit for future operations.

#### Credit Scheme
- Charge 3 units per insertion:
  * 1 unit for the actual insertion
  * 2 units saved as credit for future resizing

#### Credit Analysis
1. **Regular Operation**
   - Uses 1 unit for insertion
   - Banks 2 units for future resize

2. **During Resize**
   - Need to copy i elements when size is i
   - Have accumulated 2i units of credit (2 per insertion)
   - Credit covers the entire cost of copying

#### Proof of Correctness
```
Credit accumulated before resize of size i = 2i
Cost of resizing = i
Credit - Cost = i > 0
```

Therefore, we always have enough credit to pay for resizing.

## Conclusion

Both methods demonstrate that while a single operation might take O(n) time in the worst case (during resize), the amortized cost per operation is O(1). This makes dynamic arrays very efficient for most practical purposes.

### Takeaways
1. Individual operations can be expensive (O(n))
2. The expensive operations occur so infrequently that the average cost remains constant
3. The total cost for n operations is O(n)
4. Therefore, amortized cost per operation is O(1)