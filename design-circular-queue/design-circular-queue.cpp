class MyCircularQueue {
public:
    vector<int> data;
    int head = -1;
    int tail = -1;
    int k;
    MyCircularQueue(int k) {
        this->k=k;
        data.resize(k);
    }
    
    bool enQueue(int value) {
        if(isFull()){
            return false;
        }else{
            if(tail==k-1){
                tail=0;
                data[tail]=value;
            } else if(isEmpty()){
                head=0;
                tail=0;
                data[tail]=value;
            } else {
                tail++;
                data[tail]=value;
            }
            return true;
        }
    }
    
    bool deQueue() {
        if(isEmpty()){
            return false;
        }else{
            if(head==tail){
                data[head]=NULL;
                head = -1, tail=-1;
            }else if(head==k-1){
                data[head]=NULL;
                head=0;
            }else{
                data[head]=NULL;
                head++;
            }
            return true;
        }
    }
    
    int Front() {
        if(head!=-1){
            return data[head];
        }else{
            return -1;
        }
        
    }
    
    int Rear() {
        if(tail!=-1){
            return data[tail];
        }else{
            return -1;
        }
        
    }
    
    bool isEmpty() {
        if(head==-1 and tail==-1){
            return true;
        }else{
            return false;
        }   
    }
    
    bool isFull() {
        if((head==0 and tail==k-1) or (tail+1==head)){
            return true;
        } else{
            return false;
        }
        
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */