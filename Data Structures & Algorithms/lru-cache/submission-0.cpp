
class Node {
public:
    int key;
    int val;
    Node* prev;
    Node* next;
    Node() : key(-1), val(-1), prev(nullptr), next(nullptr) {}
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {

private:
    int capacity;
    unordered_map<int, Node *> cacheMap;
    Node* left;
    Node* right;

public:

    void remove(Node* c){
        Node* p = c->prev;
        Node* n = c->next;
        p->next = n;
        n->prev = p;
    }

    void insert(Node* c){
        Node* p = right->prev;
        p->next = c;
        right->prev = c;
        c->prev = p;
        c->next = right;
    }

    int get(int key){
        auto it = cacheMap.find(key);
        if (it == cacheMap.end()) return -1;
        remove(it->second);
        insert(it->second);
        return it->second->val;
    }

    void put(int key, int val){
        auto it = cacheMap.find(key);
        if (it != cacheMap.end()){ //contains
            it->second->val = val;
            Node* temp = it->second;
            remove(temp);
            insert(temp);
        }
        else {
            Node* newNode = new Node(key, val);
            if (cacheMap.size() == capacity){
                Node* lru = left->next;
                cacheMap.erase(lru->key); 
                remove(lru);
                        
            }
            insert(newNode);
            cacheMap[newNode->key]= newNode;
        }



    }

    
    LRUCache(int c) : capacity(c) {
        left = new Node();
        right = new Node();
        left->next = right;
        right->prev = left;
    };

};
