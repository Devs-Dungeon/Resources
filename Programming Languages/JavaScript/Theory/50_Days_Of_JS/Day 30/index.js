function wave(str) {
    // Your Code goes below
    let ans_arr = [],wrd='';
    for(let i=0;i<str.length;i++)
    {   
        if(str[i] === ' ') continue;
        wrd += str.slice(0,i) + str[i].toUpperCase() + str.slice(i+1);
        ans_arr.push(wrd);
        wrd='';
    }
  
    return ans_arr;
}

console.log(wave("hello"));
