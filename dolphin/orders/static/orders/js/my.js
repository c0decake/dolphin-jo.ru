const ordersBlock = document.getElementById('orders')

function uploadOrders() {
    ordersBlock.innerHTML = ""
    fetch('/api/v1/orders/my')
        .then(response => response.json())
        .then(orders => {
            if (orders.length > 0) {
                console.log('COT')
                orders.forEach(order => {
                    ordersBlock.append(renderOrder(order));
                })
            } else {
                let orderSection = document.createElement('section')
                orderSection.classList.add('no-order-block')
                orderSection.textContent = "У тебя нет добавленных заказов!"
                ordersBlock.append(orderSection);
            }

        })
}

function deleteOrder(order_id) {
    return new Promise((resolve, reject) => {
        fetch('/api/v1/orders/' + order_id + '/delete_my/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('meta[name="csrf_token"]').content
            }
        })
            .then(data => {
                resolve(data)
            })
            .then(error => {
                reject(error)
            })
    })
}

function renderOrder(order) {
    let orderSection = document.createElement('section')
    orderSection.classList.add('order')

    let orderId = document.createElement('span')
    orderId.classList.add('order-id')
    orderId.textContent = order['id']

    let orderDatetimeBlock = document.createElement('div')
    orderDatetimeBlock.classList.add('order-datetime')

    let orderDate = document.createElement('span')
    orderDate.classList.add('o-date')
    orderDate.textContent = order['work_date']

    let orderTime = document.createElement('span')
    orderTime.classList.add('o-time')
    orderTime.textContent = order['time_in'] + ' - ' + order['time_out']

    orderDatetimeBlock.append(orderDate, orderTime)

    let orderGeneral = document.createElement('div')
    orderGeneral.classList.add('order-general')

    let orderLocation = document.createElement('section')
    orderLocation.classList.add('o-location')

    let orderAddress = document.createElement('span')
    orderAddress.textContent = order['address']

    let orderDistrict = document.createElement('span')
    orderDistrict.textContent = order['district'] + " р-н"

    let orderCity = document.createElement('span')
    orderCity.textContent = order['city']

    orderLocation.append(orderCity, orderAddress, orderDistrict)

    let orderOther = document.createElement('section')
    orderOther.classList.add('o-other')

    let orderAdditions = document.createElement('span')
    orderAdditions.classList.add('o-additions')
    if (order['taxi_to']) {
        orderAdditions.textContent += '🚕 '
    }
    if (order['taxi_from']) {
        orderAdditions.textContent += '🚖 '
    }
    if (order['food']) {
        orderAdditions.textContent += '🍲 '
    }
    if (order['drinks']) {
        orderAdditions.textContent += '🥤 '
    }
    if (order['toilet']) {
        orderAdditions.textContent += '🚾'
    }

    let orderPost = document.createElement('span')
    orderPost.classList.add('o-post')
    orderPost.textContent = order['post_name']

    orderOther.append(orderAdditions, orderPost)

    orderGeneral.append(orderLocation, orderOther)

    let orderButton = document.createElement('section')
    orderButton.classList.add('order-button')

    let orderDetailButton = document.createElement('button')
    orderDetailButton.classList.add('my-order-btn', 'detail-btn')
    let detailImg = document.createElement('img')
    detailImg.src = staticUrl + "map-white.svg"
    orderDetailButton.append(detailImg);

    let orderEditButton = document.createElement('button')
    orderEditButton.classList.add('my-order-btn', 'edit-btn')
    let editImg = document.createElement('img')
    editImg.src = staticUrl + "pencil-white.svg"
    orderEditButton.append(editImg);

    let orderRemoveButton = document.createElement('button');
    orderRemoveButton.classList.add('my-order-btn', 'remove-btn');
    orderRemoveButton.addEventListener('click', (event) => {
        let popup = event.target.querySelector('.delete-popup')
        if (popup) {
            popup.classList.toggle('active')
            setTimeout(() => {
                popup.classList.remove('active')
            }, 3000)
        }

    })
    let trashImg = document.createElement('img')
    trashImg.src = staticUrl + "trash-white.svg"
    orderRemoveButton.append(trashImg);

    let deletePopup = document.createElement('div')
    deletePopup.classList.add('delete-popup')
    let popupQuestionSpan = document.createElement('span')
    popupQuestionSpan.textContent = "Ты уверен(-а)?"
    let popupDeleteBtn = document.createElement('button')
    popupDeleteBtn.textContent = "Удалить"
    popupDeleteBtn.addEventListener('click', (event) => {
        deleteOrder(event.target.closest('.order').querySelector('.order-id').textContent)
            .then(() => {
                uploadOrders()
            })
    })


    deletePopup.append(popupQuestionSpan, popupDeleteBtn)

    orderRemoveButton.append(deletePopup)


    orderButton.append(orderDetailButton, orderEditButton, orderRemoveButton)

    orderSection.append(orderId, orderDatetimeBlock, orderGeneral, orderButton)

    return orderSection
}

window.onload = () => {
    uploadOrders()
}
