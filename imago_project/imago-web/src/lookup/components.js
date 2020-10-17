export function loadListOrDetail(callback, page, slug) {
    const xhr = new XMLHttpRequest()
    const method = 'GET'
    let url
    if (slug) {
        url = "http://127.0.0.1:8000/api/" + page + "/" + slug
    } else {
        url = "http://127.0.0.1:8000/api/" + page + "/"
    }
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function() {
        callback(xhr.response, xhr.status)
    }
    xhr.onerror = function(e) {
        console.log(e)
        callback({"message": "There was an error"}, 400)
    }
    xhr.send()
}

export function loadImage(image_url) {
    let url = "http://localhost:8000"
    if (image_url) {
        url = url + image_url
    } else {
        url = "no image"
    }
    return url
}

export function loadCacheImage(image_filename) {
    return "http://localhost:8000/media/photologue/photos/cache/" + image_filename
}