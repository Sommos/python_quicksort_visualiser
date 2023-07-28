import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def quicksort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index))
            stack.append((pivot_index + 1, high))
            yield arr.copy()

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1

        while arr[i] < pivot:
            i += 1
        
        j -=1

        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

        yield arr

def visualise_quicksort(arr):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align = "edge")

    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * len(arr)))

    text = ax.text(0.02, 0.95, "", transform = ax.transAxes)

    def update_fig(arr, rects, text):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        
        text.set_text("Number of operations: " + str(update_fig.count))
        update_fig.count += 1
    
    update_fig.count = 0

    def animate(frame_data):
        for rect, val in zip(bar_rects, frame_data):
            rect.set_height(val)

    ani = animation.FuncAnimation(
        fig,
        func = update_fig,
        fargs = (bar_rects, text),
        # make a copy of the array to avoid mutation of the original array
        frames = quicksort(arr.copy()),
        # delay between frames in milliseconds
        interval = 50,
        repeat = False,
    )

    plt.show()

if __name__ == "__main__":
    np.random.seed(42)
    data = np.random.randint(1, 100, 20)

    visualise_quicksort(data.tolist())