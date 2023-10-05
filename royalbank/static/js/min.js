
    function myFunction() {
            var la=document.f1.lm.value
            var ir=document.f1.intra.value
            var lt=document.f1.loant.value
            var ir1=ir/12/100
            var lt1=lt*12
            var result=(la*ir1*(1+ir1)**lt1/((1+ir1)**(lt1-1)))
            document.f1.display.value=("payable ammount is"+result)
        }
