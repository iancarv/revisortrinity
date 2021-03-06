var APP = APP || {
    doInit: function () {
        this.updateStyle();
        this.doBind();
    },
    doBind: function () {
        $("#save").click(function (_this){
            return function () {
                _this.save($(this).attr('verbeteID'));
            };
        }(this));

        $("#refresh").click(function (_this){
            return function () {
                _this.refresh();
            };
        }(this));

        $(".view").click(function () {
            var cl = $( this ).attr('btn');
            $(".selected").removeClass('selected');
            $("#"+cl).addClass('selected');
        });

    },
    updateStyle: function () {
       $("#style").text($("#cssContent").text());
    },
    updateHtml: function () {
        $("#detailDescription").html($("#htmlContent").text().trim());
        $("#phonDiv").html($("#phonContent").text().trim());
    },
    refresh: function () {
        this.updateStyle();
        this.updateHtml();
    },
    saveCss: function () {
        $.post('/savecss', {css: $("#style").text()}, function (data){
            console.log(data);
        });
    },
    saveHtml: function (id) {
        console.log(id)
        console.log($("#phonContent").text())
        $.post('/savehtml', {html: $("#htmlContent").text().trim(), id: id, phonema: $("#phonContent").text().trim()}, function (data){
            console.log(data);
        });
    },
    save: function (id) {
        this.refresh();
        this.saveCss();
        this.saveHtml(id);
    }

}

$(document).ready(function() {
    APP.doInit();
});
