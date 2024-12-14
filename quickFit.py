class QuickFit:
    def __init__(self):
        # Initialize size-specific lists for memory blocks
        self.memory_blocks = {
            32: ['Block 1', 'Block 2'],
            64: ['Block 3', 'Block 4'],
            128: ['Block 5']
        }
        self.allocated = {}

    def allocate_memory(self, process, size):
        if size in self.memory_blocks and self.memory_blocks[size]:
            # Allocate from the size-specific list if available
            block = self.memory_blocks[size].pop(0)
            self.allocated[process] = (size, block)
            print(f"{process}: {size} KB allocated ({block})")
        else:
            # If no exact match, use best-fit or another strategy
            available_sizes = sorted(k for k in self.memory_blocks if self.memory_blocks[k])
            for available_size in available_sizes:
                if available_size >= size:
                    block = self.memory_blocks[available_size].pop(0)
                    self.allocated[process] = (size, block)
                    print(f"{process}: {size} KB allocated from {block} (split)")

                    # Split the block if possible
                    remaining_size = available_size - size
                    if remaining_size > 0:
                        new_block = f"New {remaining_size} KB Block from {block}"
                        self.memory_blocks.setdefault(remaining_size, []).append(new_block)
                        print(f"Created {new_block}")
                    return

            print(f"{process}: Allocation failed (no suitable block)")

    def display_memory_state(self):
        print("\nFinal Memory State:")
        print("Allocated Blocks:")
        for process, (size, block) in self.allocated.items():
            print(f"  {process}: {size} KB ({block})")

        print("Free Blocks:")
        for size, blocks in self.memory_blocks.items():
            if blocks:
                print(f"  {size} KB List: {blocks}")

# Example usage
quick_fit = QuickFit()

# User input for allocation requests
n = int(input("Enter the number of processes to allocate: "))
for _ in range(n):
    process = input("Enter process name: ")
    size = int(input(f"Enter memory size required for {process}: "))
    quick_fit.allocate_memory(process, size)

# Display the final memory state
quick_fit.display_memory_state()
