// ==UserScript==
// @name         Bing Bot - BingPoint Gathering Script (PC & Mobile)
// @namespace    http://your.homepage/
// @version      1.3 Beta
// @description  Auto Acquire Bing Rewards with Tampermonkey Chrome Extension (For Mobile Use Chrome with User-Agent Switcher)
// @author       Piradon Liengtiraphan
// @match        http://*/*
// @grant        none
// ==/UserScript==

var noun = ["Cheese", "Lamps", "Japan", "Gintama", "Marist College", "Events", "New York", "Dentist", "Optical Mouse", "Big Bang Theory", "ICS", "Bangkok", "Tokyo",
            "London", "Las Vegas", "Fallout: New Vegas", "Fallout 3", "Skyrim", "Learn", "Engineer", "Desk", "News", "Devil May Cry", "Samsung", "Apple", "Yogurt",
            "sFree", "Swensons", "Ramen", "Sushi", "Fencing", "Math", "Book", "Sheets", "Bed", "Sofa", "Banana", "Grapes", "Games", "Fish", "Microsoft", "Google",
            "Banker", "Battle", "Comb", "Editorial", "Gun", "Insurance", "Shears", "Shield", "Vegetarian", "Advice", "Bean", "Croissant", "Freezer", "Oyster", "Peak", 
            "Playroom", "Range", "Grenade", "Handsaw", "Lotion", "Maraca", "Monkey", "Nut", "Saxophone", "Thunder", "Toenail", "Trick", "earthquake", "wilderness", "dress",
            "flight", "zebra", "rings", "recess", "shock", "iron", "plane", "lunch", "suguar", "mother", "sound", "bells", "trouble", "crown", "tomatoes", "fly", "camera"]; // put your noun terms here

var verb = ["Run", "Eat", "Buy", "Purchase", "Shoot", "Jogging", "vs", "Use", "Go", "Wrestle", "Stretch", "Gaze", "Live", "Snatch", "Soothe", "Harass", "Tip", "Print", "Hate",
            "Prefer", "Trot", "Suspend", "Grip", "Allow", "Pour", "Close", "Repair", "Grate", "Pretend", "Bow", "marry", "clean", "wish", "examine", "multiply", "move", "guard",
            "injure", "paddle", "protect", "lighten", "snore", "walk", "consider", "manage", "support", "radiate", "encourage", "wait", "land", "hover", "squeak", "step", "settle",
            "slow", "melt", "hurry", "influence", "approve", "rejoice", "rush", "cycle", "practise", "ignore", "matter", "disapprove", "twist", "trade", "preach", "bolt", "educate", 
            "beam", "scribble", "relax", "found", "clip", "land", "match", "pinch", "stamp", "continue", "fit", "realise", "wonder", "buzz", "spoil", "beam", "sack", "amuse", "file",
            "permit", "attempt", "correct", "kick", "bake", "answer", "fasten", "lighten", "ski"]; //put your verbs here

if(window.location == "http://www.bing.com/") {
    var i = parseInt(Math.random() * noun.length);
    var u = parseInt(Math.random() * noun.length);
    var o = parseInt(Math.random() * verb.length);
    document.getElementById("sb_form_q").value = noun[i] + " " + verb[o] + " " + noun[u];
    document.getElementById("sb_form_go").click();
    if(document.getElementById('sb_form_go') === null){
        document.getElementById('sbBtn').click();
    };
};

if(window.location != "http://www.bing.com/") {
    var i = parseInt(Math.random() * noun.length);
    var u = parseInt(Math.random() * noun.length);
    var o = parseInt(Math.random() * verb.length);
    document.getElementById("sb_form_q").value = noun[i] + " " + verb[o] + " " + noun[u];
    document.getElementById("sb_form_go").click();
    if(document.getElementById('sb_form_go') === null){
        document.getElementById('sbBtn').click();
    };
};

//document.getElementById('id_rh').click;