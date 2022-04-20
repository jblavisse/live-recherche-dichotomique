
let t = [3, 7, 11, 15, 22, 37];
let val = 37;

let trv = false;

let deb = 0;
let fin = t.length-1;

let pos=-1;

while(!trv && deb <= fin) {
    let mil = Math.floor((deb+fin)/2);

    if(t[mil] == val) {
        trv = true;
        pos = mil;
    }

    else if(t[mil] < val) {
        deb = mil+1;
    }

    else if(t[mil] > val) {
        fin = mil-1;
    }

}


console.log(pos);