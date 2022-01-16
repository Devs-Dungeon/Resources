function high(x) {
    //code your magic here
    x = x.split(' ');
    let mx = 0,mx_word,curr=0;
    x.forEach((wrd) => {
        wrd = wrd.split('');
        wrd.forEach((letter) => {
            curr = curr + letter.charCodeAt(0) - 96;
        });
        if(mx<curr)
        {
            mx = curr;
            mx_word = wrd.join('');
        }
        curr = 0;
    });
    
    return mx_word;
}
