
function get_shareable_link() {
    console.log()
    let link_info_part = "share/" + document.getElementById("username").innerHTML + "/"

    let link = window.location.href
    if (window.location.href.includes("share")) {
        let x = link.split("share")
        link = x[0] + link_info_part
        document.getElementById("link_paragraph").innerHTML = link

    } else {
        let link = window.location.href + link_info_part
        document.getElementById("link_paragraph").innerHTML = link
        console.log(link)
    }


}


function copy_link() {

    // copies to clipboard only works if link is secured or when in localhost
    navigator.clipboard.writeText(document.getElementById("link_paragraph").innerHTML)
}