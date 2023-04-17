
let myInit = {
    method : 'GET',
    headers : {
        'Content-Type'  : 'application/json'
    },
    mode : 'cors',
    cache : 'default'
}

let myRequest = new Request("./test.json" , myInit)
 
fetch(myRequest)
.then(res => res.json())
.then(data => {console.log(data.set)});

function showInfo(data){
    console.table(data)
}

