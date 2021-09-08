/* JS for tab "workshop dataset" card */
class WorkShopData_Card {

    constructor({id, wk_title, wk_source}) {
        this._id = id + "";
        // this._title = wk_title + "";
        // this._source = wk_source + "";
    }

    _createCard () {
        let deck_single_node = document.createElement("div");
        let card = document.createElement("div");
        let cardBorder=`<div class="workshop-card-border"></div>`
        let cardImg_Html = `<div class="workshop-card-img-top"><img src="./assets/image/workshop_img/${this._id}.jpg"></div>`;
        // let card_body = document.createElement("div");
        // let cardTitle_Html = `<div class="workshop-card-title">${this._title}</div>`;
        // let cardText_Html = `<div class="workshop-card-text"><p>${this._source}</p>`;

        deck_single_node.classList.add("col", "workshop-deck-single");
        card.classList.add("worksop-card");
        // card_body.classList.add("worksop-card-body");
        // card_body.innerHTML = cardTitle_Html + cardText_Html;
        card.innerHTML = cardBorder+cardImg_Html;
        // card.appendChild(card_body);
        
        deck_single_node.appendChild(card);
        return deck_single_node;
    }

    _bindEvents () {
        if(this._deck_single_node === undefined) {
            console.error("Workshop dataset card do not exist!");
        }
        // tooltip binding to card title
        // $(this._deck_single_node.querySelector(".card-title")).tooltip({ title: this._title });
    }
}

WorkShopData_Card.prototype.appendTo = function (parentNode, nextNode) {
    if(!(parentNode instanceof HTMLElement)) {
        console.error(`${parentNode} is not a DOM node!`);
        return false;
    }

    this._deck_single_node = this._createCard();
    this._bindEvents();

    parentNode.insertBefore(this._deck_single_node, nextNode);
    return true;
}

export {WorkShopData_Card as WorkShopData_Card};