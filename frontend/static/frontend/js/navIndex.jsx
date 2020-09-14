const { useState, Fragment } = React;

const NavLink = ({ link }) => {
  return (
    <li className="mobile-nav__item">
      <a
        href={`${window.location.origin}/${Object.values(link)[0]}`}
        className="mobile-nav__link"
      >
        {Object.keys(link)[0]}
      </a>
    </li>
  );
};

const MobileNav = ({ links }) => {
  return (
    <div className="mobile-nav__inner">
      <ul className="mobile-nav__list">
        {links.map((item, index) => (
          <NavLink key={index} link={item} />
        ))}
      </ul>
      <ul>
        <li className="mobile-nav__item"><a href="" className="mobile-nav__link">kek</a></li>
        <li className="mobile-nav__item"><a href="" className="mobile-nav__link">kek</a></li>
      </ul>
    </div>
  );
};

const addresses = [
  { "О Компании": "o-kompanii/" },
  { Продукция: "" },
  { "Полезная информация": "poleznaya-informaciya/" },
  { Сертификаты: "sertifikaty/" },
  { "Наши работы": "nashi-raboty/" },
  { Контакты: "kontakty/" },
];

ReactDOM.render(
  <MobileNav links={addresses} />,
  document.getElementById("mobile-nav")
);

const Burger = () => {
  const [toggler, setToggler] = useState(false);
  const nav = document.getElementsByClassName("mobile-nav")[0];
  const site = document.getElementsByClassName("site-section")[0];
  const body = document.body
  const menuOff = () => {
    nav.className = 'mobile-nav'
    site.className = 'site-section'
    body.style.overflow = 'scroll' 
  }
  const burgerClick = () => {
    if (!toggler) {
      nav.className += ' nav-open'
      site.className += ' mobile-nav-open'
      body.style.overflow = 'hidden'
      site.addEventListener('touchstart', menuOff, { capture: true, passive: true })
    } else {
      nav.className = 'mobile-nav'
      site.className = 'site-section'
      body.style.overflow = 'scroll'
      site.removeEventListener('touchstart', menuOff, { capture: true, passive: true })
      setToggler(!toggler);
    }
  };
  return (
    <div onClick={() => burgerClick()} className="burger">
      <span></span>
    </div>
  );
};

ReactDOM.render(<Burger />, document.getElementById("burger-wrapper"));
