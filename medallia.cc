[0,2,4,6]
[1,3,5,7]
...
...

bandwidth: 1Gbps
latency: 0.5ms
1000 machines
each contains 1 million integers
log(1,000,000,000,000)= 20 in each
running time 1000 * 20 = 20,000


find index of value k in the combined sorted list.
[0,2,4,6] mid_1 = 2, index_1 = 1
[1,3,5,7] mid_2 = 3, index_2 = 1
th element, value = 5
value > mid_1 and mid_2
start_1 = mid_1 + 1
start_2 = mid_2 + 1

kth = index_1 + index_2

vector<T> vec;
list<T>

//////////////////////////////////////

class vector<T> {
private:
    T[] array;
    int current_size;
    int size;
        
public:
void pushback(T t) {
    if ((current_size + 1) >= size) {
        T[] new_array = new T[2 * size];
        for (int i = 0; i < size; i++) {
            new_array[i] = array[i];
        }
        current_size ++;
        new_array[current_size] = t;
        array = new_array;
        size *= 2;                 //O(size)  
    } else {
        array[current_size++] = t; //O(1)
    }
}
n / 2 + n / 4 + .... + 1 = n ( 1 + ... + 1/2^k) =  n  
O(n)

class Node <T> {
    T val;
    Node* next;
    Node(T val) {
        this.val = val;
    }
}
class list<T> {
private:
    Node head;
    Node tail;

void pushback(T t) {
    Node node = new Node(t); // 
    tail.next = node;
    tail = node;
}
