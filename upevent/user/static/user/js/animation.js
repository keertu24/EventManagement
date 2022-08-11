const animate = document.querySelector('.anime');
    const animateRight = document.querySelector('.animeRight');
    animate.classList.remove('animate__slideInLeft')
    animateRight.classList.remove('animate__slideInRight')
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            const animate = entry.target.querySelector('.anime');
            const animateRight = entry.target.querySelector('.animeRight');
            if (entry.isIntersecting) {
                animate.classList.add('animate__slideInLeft');
                animateRight.classList.add('animate__slideInRight');
                return;
            }
            animate.classList.remove('animate__slideInLeft')
            animateRight.classList.remove('animate__slideInRight')
        });
    });
    observer.observe(document.querySelector('.cls-head'));


    const animate2 = document.querySelector('.anime');
    const animateRight2 = document.querySelector('.animeRight');
    animate2.classList.remove('animate__slideInLeft')
    animateRight.classList.remove('animate__slideInRight')
    const observer2 = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            const animate2 = entry.target.querySelector('.anime');
            const animateRight2 = entry.target.querySelector('.animeRight');
            if (entry.isIntersecting) {
                animate2.classList.add('animate__slideInLeft');
                animateRight2.classList.add('animate__slideInRight');
                return;
            }
            animate2.classList.remove('animate__slideInLeft')
            animateRight2.classList.remove('animate__slideInRight')
        });
    });
    observer.observe(document.querySelector('.cls-head2'));

    const animate3 = document.querySelector('.anime');
    const animateRight3 = document.querySelector('.animeRight');
    animate2.classList.remove('animate__slideInLeft')
    animateRight.classList.remove('animate__slideInRight')
    const observer3 = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            const animate3 = entry.target.querySelector('.anime');
            const animateRight3 = entry.target.querySelector('.animeRight');
            if (entry.isIntersecting) {
                animate3.classList.add('animate__slideInLeft');
                animateRight3.classList.add('animate__slideInRight');
                return;
            }
            animate3.classList.remove('animate__slideInLeft')
            animateRight3.classList.remove('animate__slideInRight')
        });
    });
    observer.observe(document.querySelector('.cls-head3'));