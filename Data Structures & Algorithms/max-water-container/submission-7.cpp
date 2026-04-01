class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left=0;
        int right=heights.size()-1;
        int maxi=0;
        int vol=0;

        while(left<right)
        {
            int height=min(heights[right],heights[left]);
            vol=(right-left)*height;
            if(heights[left]<=heights[right])
            {
                left++;
            }
            else{
                right--;
            }
            maxi=max(maxi,vol);
            
        }
        return maxi;
    }
};

