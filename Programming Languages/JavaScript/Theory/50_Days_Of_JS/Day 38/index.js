const valid = (string) => {
	// code here
    let p = (string.trim().split('')).filter((val)=>val!==" ");
    for(let i of p)
        if(isNaN(i)) return false;

    let s=[];
    p.reverse();
    for(let i=0;i<p.length;i++)
    {
        if(i%2 !== 0)
            s += (((Number(p[i])*2)>9)?(Number(p[i])*2 - 9):(Number(p[i])*2)).toString();
        else 
            s += p[i];
    }

    let sum=0;
    s = s.split('');
    s.forEach((v)=>{
        sum += Number(v);
    });
    
	return (sum%10 ===0)
}
