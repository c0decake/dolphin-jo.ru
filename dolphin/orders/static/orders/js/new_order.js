fetch('/api/v1/shops/my')
    .then(response => response.json())
    .then(shops => {
        if (shops.length > 0) {
            let shopSelector = document.getElementById('shop-selector')
            shops.forEach(shop => {
                let shopOption = document.createElement('option')
                shopOption.value = shop.id
                shopOption.textContent = shop.address
                shopSelector.append(shopOption)
            })
        }
    })

fetch('/api/v1/posts')
    .then(response => response.json())
    .then(posts => {

        let postSelector = document.getElementById('post-selector')
        posts.forEach(shop => {
            let postOption = document.createElement('option')
            postOption.value = shop.id
            postOption.textContent = shop.name
            postSelector.append(postOption)
        })
    })