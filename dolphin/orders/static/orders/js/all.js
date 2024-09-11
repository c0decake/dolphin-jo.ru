const ordersContainer = document.getElementById('orders')

function load_orders() {
    const wsUrl = 'ws://' + window.location.host + '/ws/orders/';
    const socket = new WebSocket(wsUrl);

    socket.onmessage = (event) => {
        let response = JSON.parse(event.data)

        if (response['type'] === "status") {
            console.log(response['status'])
        }
        else if (response['type'] === "orders") {
            ordersContainer.innerHTML = ''
            response['orders'].forEach(order => {
                renderOrder(order)
            })
        }
    };

    socket.onerror = (error) => {
        console.error('WebSocket error :', error);
    };
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
    console.log(order)
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

    let orderTakeButton = document.createElement('button')
    orderTakeButton.classList.add('take-btn')
    orderTakeButton.textContent = order['price'] + 'р'

    orderButton.append(orderTakeButton)

    orderSection.append(orderId, orderDatetimeBlock, orderGeneral, orderButton)


    ordersContainer.append(orderSection)
}


// document.addEventListener('DOMContentLoaded', () => {
//     let socket = wsConnect()
//
//     let allOrders = document.getElementById("all-orders-tab")
//     let addedOrders = document.getElementById("added-orders-tab")
//
//     allOrders.addEventListener("click", () => {
//         if (!allOrders.classList.contains("all-orders-tab_active")) {
//             socket = wsConnect()
//             document.getElementById('orders').innerHTML = ""
//             allOrders.classList.add("all-orders-tab_active")
//             addedOrders.classList.remove("added-orders-tab_active")
//         }
//     })
//
//     addedOrders.addEventListener("click", () => {
//         if (!addedOrders.classList.contains("added-orders-tab_active")) {
//             socket.close()
//             document.getElementById('orders').innerHTML = ""
//             addedOrders.classList.add("added-orders-tab_active")
//             allOrders.classList.remove("all-orders-tab_active")
//
//
//             fetch("/api/orders/my")
//                 .then(response => response.json())
//                 .then(orders => orders.forEach(order => {
//                     renderOrder(order)
//                 }))
//         }
//     })
// });


window.onload = () => {
    load_orders()
}