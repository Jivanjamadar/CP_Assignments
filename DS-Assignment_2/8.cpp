//Submission ID : 1277688857

class BrowserHistory {
public:
    vector<string> arr;
    int curr ;

    BrowserHistory(string hp) {
        curr = 0;
        arr.push_back(hp);
    }
    
    void visit(string url) {
        int end = arr.size()-1;
        while(end>curr){
            arr.pop_back();
            end--;
        }
        curr++;
        arr.push_back(url);
    }
    
    string back(int steps) {
        curr = max(0,curr-steps);
        return arr[curr];
    }
    
    string forward(int steps) {
        int end = arr.size()-1;
        curr = min(end,curr+steps);
        return arr[curr];
    }
};
