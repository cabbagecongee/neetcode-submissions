class DynamicArray {
    public int size;
    public int arr_cap;
    int[] array;

    public DynamicArray(int capacity) {
        array = new int[capacity];
        size = 0; 
        arr_cap = capacity;
    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        array[i] = n;
    }

    public void pushback(int n) {
        if (size >= arr_cap){
            resize();
        }
        array[size] = n;
        size++;
    }

    public int popback() {
        int n  = array[size-1];
        size--;
        return n; 
    }

    private void resize() {
        arr_cap = arr_cap * 2;
        int[] new_arr = new int[arr_cap];
        for (int i = 0; i < size; i++){
            new_arr[i] = array[i];
        }
        array = new_arr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return arr_cap;
    }
}
