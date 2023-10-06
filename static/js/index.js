async function getProducts() {
  $(".new-book-notif").hide();
  return fetch("/get-product").then((res) => res.json());
}


async function refreshProducts() {
  const items = await getProducts();
  let stringAdd = "";
  
  items.forEach((item) => {
    stringAdd += `<article class="col buku"><div class="card text-white bg-dark shadow-sm"><div class="card-body"><a href="/delete/${item.pk}"><button type="submit" class="btn-close btn-close-white position-absolute top-0 end-0 me-2 mt-2"></button></a><h5 class="card-title fw-bold">${item.fields.name}</h5><p class="card-text">${item.fields.description}</p><div class="d-flex justify-content-between align-items-center"><div class="btn-group"><a href="/add_stock/${item.pk}" type="button" class="btn btn-sm btn-outline-light">+</a><a href="/sub_stock/${item.pk}" type="button" class="btn btn-sm btn-outline-light">-</a></div><small class="text-white">${item.fields.amount}</small></div></div></div></article>`;
    
    $(".bookshelf").html(stringAdd);
  });
}

function addItem() {
  fetch("/create-ajax/", {
    method: "POST",
    body: new FormData(document.querySelector("#form-add-buku")),
  }).then(refreshProducts);

  document.querySelector("#form-add-buku").reset();
  $(".new-book-notif").show();
  return false;
}

function addProduct() {
  fetch("{% url 'main:add_product_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#form'))
  }).then(refreshProducts)

  document.getElementById("form").reset()
  return false
}

if (window.location.href.indexOf("main") != -1) {
  refreshProducts();
}

$("#button_add").click(addItem);
