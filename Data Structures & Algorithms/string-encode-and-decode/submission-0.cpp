class Solution {
public:

    string encode(vector<string>& strs) {
        vector<int> arr;
        for(const string &str:strs)
            {
                int length = str.size();
                arr.push_back(length);
            }
        string encoded = "";
        for(int i=0;i<arr.size();i++)  
            {
                encoded += to_string(arr[i])+"#"+strs[i];
            }  
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> strs;
        int i = 0;
        while(i < s.size())
            {
               int j = s.find('#',i); //position of # will be in j search for # will start from i
               int len = stoi(s.substr(i,j));
               string word = s.substr(j + 1,len);
               strs.push_back(word);
               i=j+1+len;
            }
        return strs;
    }
};
