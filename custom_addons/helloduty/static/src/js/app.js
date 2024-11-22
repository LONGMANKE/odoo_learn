// ------------------------ Design ------------------------

const buttonId = "helloduty-cti-dialer-button";
const dialerId = "helloduty-cti-dialer";
const containerId = "helloduty-cti-dialer-container";

const dialerButton = document.createElement("div");
const dialer = document.createElement("div");
const dialerContainer = document.createElement("div");

const opensvg =
  '<svg id="call" viewBox="0 0 24 24" fill="#ffffff" xmlns="http://www.w3.org/2000/svg"><path d="M24,18v3.62A2.41,2.41,0,0,1,21.56,24h-.23a23.81,23.81,0,0,1-10.39-3.7,23.46,23.46,0,0,1-7.23-7.21A24,24,0,0,1,0,2.62,2.4,2.4,0,0,1,2.19,0H6A2.41,2.41,0,0,1,8.43,2.06a16.48,16.48,0,0,0,.84,3.39A2.39,2.39,0,0,1,8.74,8L7.2,9.52a19.44,19.44,0,0,0,7.23,7.23L16,15.27a2.42,2.42,0,0,1,2.55-.59,15.63,15.63,0,0,0,3.38.84A2.41,2.41,0,0,1,24,18Z"/></svg>';
const closesvg =
  '<svg id="act-close" viewBox="0 0 320 512" fill="#ffffff" xmlns="http://www.w3.org/2000/svg"><path d="M310.6 361.4c12.5 12.5 12.5 32.75 0 45.25C304.4 412.9 296.2 416 288 416s-16.38-3.125-22.62-9.375L160 301.3L54.63 406.6C48.38 412.9 40.19 416 32 416S15.63 412.9 9.375 406.6c-12.5-12.5-12.5-32.75 0-45.25l105.4-105.4L9.375 150.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 210.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-105.4 105.4L310.6 361.4z"/></svg>';

const manageClickEvent = (ev, cb) => {
  let num = "";

  if (
    ev.target &&
    ev.target.tagName !== undefined &&
    ev.target.tagName === "A" &&
    ev.target.outerHTML.includes('href="tel:')
  ) {
    num = ev.target.pathname;
  } else if (
    ev.target &&
    ev.target.parentElement !== undefined &&
    ev.target.parentElement !== null &&
    ev.target.parentElement.tagName !== undefined &&
    ev.target.parentElement.tagName !== null &&
    ev.target.parentElement.tagName === "A" &&
    ev.target.parentElement.outerHTML.includes('href="tel:')
  ) {
    num = ev.target.parentElement.pathname;
  }

  if (num !== "") {
    ev.preventDefault();
    ev.stopImmediatePropagation();
    ev.stopPropagation();
    show();
    cb(num);
  }
};

const show = () => {
  dialerContainer.style.opacity = "1";
  dialerContainer.style.maxHeight = "100%";
  dialerContainer.style.transform = null;
  dialerButton.innerHTML = closesvg;
};

const hide = () => {
  dialerContainer.style.opacity = "0";
  dialerContainer.style.maxHeight = "0";
  dialerContainer.style.transform = "scale(0)";
  dialerButton.innerHTML = opensvg;
};

const toggle = (ev) => {
  ev.preventDefault();
  ev.stopImmediatePropagation();
  ev.stopPropagation();
  if (Number(dialerContainer.style.opacity) !== 0) {
    hide();
  } else {
    show();
  }
};

const design = () => {
  console.log("Start Design");
  dialerContainer.id = containerId;
  dialerContainer.style.bottom = "4.5rem";
  dialerContainer.style.zIndex = "9999";
  dialerContainer.style.right = "0.6rem";
  dialerContainer.style.borderRadius = "8px";
  dialerContainer.style.padding = "2px";
  dialerContainer.style.marginRight = "1rem";
  dialerContainer.style.background = "#fdfdfd";
  dialerContainer.style.boxShadow = "0 5px 40px rgba(0,0,0,.16)";
  dialerContainer.style.position = "fixed";
  dialerContainer.style.border = "none";
  dialerContainer.style.opacity = "1";
  dialerContainer.style.transition =
    "width .2s ease 0s,height .2s ease 0s,max-height .2s ease 0s,transform .3s cubic-bezier(0,1.2,1,1) 0s,opacity 83ms ease-out 0s";
  dialerContainer.allow = "microphone;autoplay;clipboard-read;clipboard-write;";

  dialerButton.id = buttonId;
  dialerButton.style.backgroundRepeat = "no-repeat";
  dialerButton.style.backgroundSize = "contains";
  dialerButton.style.backgroundPosition = "center center";
  dialerButton.style.borderRadius = "50%";
  dialerButton.style.boxSizing = "border-box";
  dialerButton.style.zIndex = "9999";
  dialerButton.style.display = "flex";
  dialerButton.style.backgroundColor = "#1C68F4";
  dialerButton.style.width = "40px";
  dialerButton.style.height = "40px";
  dialerButton.style.cursor = "pointer";
  dialerButton.style.backgroundOrigin = "content-box";
  dialerButton.style.padding = "10px";
  dialerButton.style.boxShadow = "0px 2px 10px rgba(54, 205, 207, 0.4)";
  //   dialerButton.style.display = "none";

  dialer.id = dialerId;
  dialer.appendChild(dialerContainer);
  dialer.appendChild(dialerButton);
  dialer.style.display = "flex";
  dialer.style.flexDirection = "column";
  dialer.style.position = "fixed";
  dialer.style.right = "1rem";
  dialer.style.bottom = "0.6rem";
  dialer.style.zIndex = "9999";
  dialer.style.alignItems = "flex-end";
  dialer.style.gap = "0.8rem";

  dialerButton.addEventListener("click", (ev) => toggle(ev));
  document.body.appendChild(dialer);
};

// ------------------------ Design ------------------------

// ------------------------ Logic ------------------------

let cti;
let currentuser = {};
let currentcall = {};
let settings;

function getToken() {
  return new Promise((resolve, reject) => {
    $.ajax({
      url: "/helloduty/settings",
      type: "POST",
      data: JSON.stringify({}),
      dataType: "json",
      contentType: "application/json",
      success: function (data) {
        resolve(data.result);
      },
      error: function (data) {
        reject(data);
      },
    });
  });
}

function loadScript() {
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src = "https://cti.helloduty.com/lib/helloduty-cti.js";
  script.onload = initiateSdk;
  document.body.prepend(script);
}

function createContact({ phoneNumber }) {
  return new Promise((resolve, reject) => {
    $.ajax({
      url: "/helloduty/api/contact/create",
      type: "POST",
      data: JSON.stringify({
        jsonrpc: "2.0",
        params: {
          phone: phoneNumber,
          name: `New caller [${phoneNumber}]`,
        },
      }),
      dataType: "json",
      contentType: "application/json",
      success: function (data) {
        resolve(data.result.contact);
      },
      error: function (data) {
        reject(data);
      },
    });
  });
}

function searchContact({ phoneNumber }) {
  return new Promise((resolve, reject) => {
    $.ajax({
      url: `/helloduty/api/contact`,
      type: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      data: JSON.stringify({
        jsonrpc: "2.0",
        params: {
          phone: `${phoneNumber.replace("+", "")}`,
        },
      }),
      dataType: "json",
      success: function (data) {
        resolve(data.result.contact);
      },
      error: function (data) {
        reject(data);
      },
    });
  });
}

function initiateSdk() {
  getToken()
    .then((settings) => {
      settings = settings;

      cti = new BrrngCti.Client(settings?.token, {
        tokenType: "user",
        selector: `#${containerId}`,
      });

      cti.on("OnLoad", () => {
        setSize();
      });

      cti.on("OnRefit", handleOnRefit);
      cti.on("MissingToken", handleMissingToken);
      cti.on("OnCallRinging", handleOnCallRinging);
      cti.on("OnCallFinish", handleOnCallFinish);
      cti.on("OnCallConnected", handleOnCallConnected);
      // cti.on("OnCallEnded", handleOnCallEnd);
      // cti.on("OnLoad", handleOnLoad);
      // cti.on("OnAgentStatusChange", handleAgentStatusChange);
    })
    .catch((error) => {
      console.error("An error occurred getting the token", error);
    });
}

function setSize() {
  const saveDimensions = (w, h) => {
    localStorage.setItem(
      "dimensions",
      JSON.stringify({
        width: w,
        height: h,
      })
    );
  };

  const loadDimensions = () => {
    const savedDimensions = localStorage.getItem("dimensions");
    if (savedDimensions) {
      return JSON.parse(savedDimensions);
    }

    const windowHeight = window.windowHeight;
    const height = windowHeight > 504 ? 504 : windowHeight;
    const windowWidth = window.windowWidth;
    const width = windowWidth > 384 ? 384 : windowWidth;

    return { width, height };
  };

  const dimensions = loadDimensions();
  saveDimensions(dimensions.width, dimensions.height);

  cti.getSize({
    height: Math.ceil((dimensions.height * 100) / window.outerHeight),
    width: Math.ceil((dimensions.width * 100) / window.outerWidth),
  });

  dialerContainer.style.width = `${dimensions.width}px`;
  dialerContainer.style.height = `${dimensions.height}px`;
}

function handleOnRefit({ payload }) {
  payload.width = payload.width > 100 ? 20 : payload.width;
  payload.height = payload.height > 100 ? 50 : payload.height;

  var finalWidth = (window.outerWidth * payload.width) / 100;
  var finalHeight = (window.outerHeight * payload.height) / 100;

  if (finalHeight < 504 || finalWidth < 384) {
    if (finalHeight < 504) {
      finalHeight = 504;
    }

    if (finalWidth < 384) {
      finalWidth = 384;
    }

    cti.getSize({
      height: Math.ceil((finalHeight * 100) / window.outerHeight),
      width: Math.ceil((finalWidth * 100) / window.outerWidth),
    });
  }

  dialerContainer.style.width = `${finalWidth}px`;
  dialerContainer.style.height = `${finalHeight}px`;

  localStorage.setItem(
    "dimensions",
    JSON.stringify({
      width: finalWidth,
      height: finalHeight,
    })
  );
}

function handleMissingToken() {
  $.ajax({
    url: "/helloduty/api/user",
    type: "POST",
    data: JSON.stringify({
      jsonrpc: "2.0",
      params: {},
    }),
    dataType: "json",
    contentType: "application/json",
    success: function (data) {
      currentuser = data.result;
      cti.authenticate(data.result.user_id, data.result.user_name);
    },
    error: function (data) {
      console.error(data);
    },
  });
}

async function handleOnCallRinging({ payload }) {
  if (payload.direction === "Outgoing") {
    const { phoneNumber, externalId, relatedRecord } = payload;
    if (externalId && externalId !== relatedRecord?.id) {
      popTicketOrContact(externalId);
    } else {
      await searchContact({ phoneNumber }).then(async (contact) => {
        if (contact) {
          cti.setName(phoneNumber, contact.name);
          popTicketOrContact(contact.id);
        } else {
          await createContact({ phoneNumber }).then((contact) => {
            if (contact) {
              cti.setName(phoneNumber, contact.name);
              popTicketOrContact(contact.id);
            }
          });
        }
      });
    }

    $.ajax({
      url: "/helloduty/api/call_activity/create",
      type: "POST",
      data: JSON.stringify({
        jsonrpc: "2.0",
        params: {
          contactid: currentcall.contactId,
          notes: `Started a call to ${phoneNumber} at ${new Date(
            new Date().toString().split("GMT")[0] + " UTC"
          )
            .toISOString()
            .split(".")[0]
            .replace("T", " ")}.`,
        },
      }),
      dataType: "json",
      contentType: "application/json",
      success: function (data) {
        currentcall.activity = data.result.activity;
      },
      error: function (data) {
        console.error(data);
      },
    });
  }
}

function handleOnCallConnected({ payload }) {
  popTicketOrContact(payload.externalId);
}

async function handleOnCallFinish({ payload }) {
  if (currentcall?.activity?.id) {
    $.ajax({
      url: "/helloduty/api/call_activity/finish",
      type: "POST",
      data: JSON.stringify({
        jsonrpc: "2.0",
        params: {
          id: currentcall.activity.id,
          notes: `Notes: ${payload.notes}\n\nCall completed at ${new Date(
            new Date().toString().split("GMT")[0] + " UTC"
          )
            .toISOString()
            .split(".")[0]
            .replace("T", " ")}.`,
        },
      }),
      dataType: "json",
      contentType: "application/json",
      success: function () {
        popTicketOrContact(currentcall.contactId);
        currentcall = {};
      },
      error: function (data) {
        currentcall = {};
        console.error(data);
      },
    });
  }
}

function popTicketOrContact(id) {
  currentcall.contactId = id;
  window.location.href = `/web#id=${id}&cids=1&model=res.partner&view_type=form`;
}

// ------------------------ Logic ------------------------

function mainFun() {
  document.addEventListener(
    "click",
    (ev) =>
      manageClickEvent(ev, (num) => {
        cti.dial(num, false);
      }),
    false
  );
  design();
  loadScript();
  hide();
}

$(document).ready(function () {
  mainFun();
});
