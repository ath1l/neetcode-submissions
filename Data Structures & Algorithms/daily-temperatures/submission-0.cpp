class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {

        vector<int> result;
        for(int i=0;i<temperatures.size();i++)
                    {
                        int crntTemp = temperatures[i];
                        int counter =0;
                        int flag = 0;
                        for(int j=i+1; j<temperatures.size(); j++)
                            {
                                if(temperatures[j]>crntTemp)
                                    {
                                        flag = 1;
                                        counter++;
                                        result.push_back(counter);
                                        break;
                                    }
                                else{
                                    counter++;
                                }
                            }
                        if(flag == 0)
                            {
                                result.push_back(0);
                            }
                    }
                return result;
     
    }
};
