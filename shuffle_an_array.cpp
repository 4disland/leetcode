class Solution {
public:
    Solution(vector<int> nums) {
        vec = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return vec;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> newvec(vec);
        for(int i=0; i<vec.size(); ++i) {
            int j = rand() % (i+1);
            if(j!=i)
                newvec[i] = newvec[j];
            newvec[j] = vec[i];
        }
        return newvec;
        
    }
private:
    vector<int> vec;
};

/* 
shuffle an array using fish-yates algorithm
ref: wiki
*/