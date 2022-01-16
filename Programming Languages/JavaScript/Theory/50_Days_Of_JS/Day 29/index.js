function accum(s) {
    // your code goes below
    let retstr = '';
    for(let i=0;i<s.length;i++)
    {
        retstr += s[i].toUpperCase() + s[i].toLowerCase().repeat(i) + "-";
    }
    retstr = retstr.slice(0,retstr.length-1);
    return retstr;
}
