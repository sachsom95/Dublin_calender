
introJs().setOptions({
    steps: [{
        intro: "Lets get started with the cloud tour give me an A+"
    },
    {
        element: document.querySelector('#add_tour'),
        intro: "Click this button to make new events"
    }, {
        element: document.querySelector('#edit_tour'),
        intro: "Modify with impunity"
    }, {
        element: document.querySelector('#delete_tour'),
        intro: "Dont worry PostGres Db will take care of it"
    }, {
        element: document.querySelector('#search_tour'),
        intro: "Okay the search is still not working but hey I am working on it"
    }, {
        element: document.querySelector('#share_tour'),
        intro: "Show em how busy you are!! "
    }, {
        element: document.querySelector('#logout_tour'),
        intro: "please dont logout :( "
    }



    ]
}).start();
