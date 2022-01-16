function getCount(str) {
    let vowelsCount = 0;
    str = str.toLowerCase();
    // enter your magic here
    let arr = str.split('');
    arr.forEach((a) => {
        if(a==='a' || a==='e' || a==='i' || a==='o' || a==='u')
          vowelsCount++;
    })
    return vowelsCount;
}

console.log(getCount("abracadabra"));
