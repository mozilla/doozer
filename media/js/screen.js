$(document).ready(function() {
  setTimeout(function() {
    $('#messages').slideUp('slow');
  }, 3000);

  $(".tile-list .game p").vtruncate();

  // TODO(potch) unsuckify
  // var to = false;
  // var $hoverEl = $("<div>barf").hide().appendTo($('.games'));
  // $(".games .game").mouseover(function() {
  //     var $tgt = $(this);
  //     // if ($tgt.find('p').attr('oldtext')) return;
  //     // if (to) clearInterval(to);
  //     // to = setTimeout(function() {
  //         var pos = $tgt.position();
  //         $hoverEl = $tgt.clone();
  //         $hoverEl.css({
  //             position: 'absolute',
  //             top: pos.top,
  //             left: pos.left,
  //             background: 'url("/media/img/tile.png")',
  //             'pointer-events': 'none',
  //         });
  //         $hoverEl.show();
  //     // }, 300);
  // });
  // $(".games .game").mouseout(function() {
  //     // clearTimeout(to);
  //     // to = false;
  //     $hoverEl.hide();
  // });
});
