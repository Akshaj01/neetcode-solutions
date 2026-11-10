class KthLargest {

private:

    int heap_size;
    priority_queue<int, vector<int>, greater<int>> k_heap;

public:
    
    KthLargest(int k, vector<int> & nums){
        heap_size = k;
        for(int i : nums){
            k_heap.push(i);
        }
    }
    
    int add(int val) {
        k_heap.push(val);
        while (k_heap.size() > heap_size){
            k_heap.pop();
        }
        return k_heap.top();
    }

};
