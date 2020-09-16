const { useState, Fragment } = React;

const NavLink = ({ link, toggleSubmenu }) => {
  return Object.keys(link)[0] == "Продукция" ? (
    <li className="mobile-nav__item" onClick={() => toggleSubmenu("-240px")}>
      <a
        href={`${window.location.origin}/${Object.values(link)[0]}`}
        className="mobile-nav__link"
        onClick={(e) => e.preventDefault()}
      >
        {Object.keys(link)[0]}
        <i className="icon-chevron-right"></i>
      </a>
    </li>
  ) : (
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

const SubMenu = ({ toggleSubmenu }) => {
  return (
    <ul className="mobile-subnav">
      <li
        className="mobile-nav__item mobile-nav__back"
        onClick={() => toggleSubmenu("0")}
      >
        <i className="icon-chevron-left"></i>
      </li>
      <li className="mobile-nav__item mobile-nav__title">Смеси для</li>
      <li className="mobile-nav__item">
        <a href={`${window.location.origin}/smesi-dlya-utepleniya/`}>
          Утепления
        </a>
      </li>
      <li className="mobile-nav__item">
        <a href={`${window.location.origin}/smesi-dlya-pola/`}>Пола</a>
      </li>
      <li className="mobile-nav__item">
        <a href={`${window.location.origin}/kladochnye-smesi/`}>Кладки</a>
      </li>
      <li className="mobile-nav__item">
        <a href={`${window.location.origin}/smesi-dlya-oblicovki/`}>
          Облицовки
        </a>
      </li>
      <li className="mobile-nav__item">
        <a href={`${window.location.origin}/shtukaturnye-smesi/`}>Штукатурки</a>
      </li>
    </ul>
  );
};

const MobileNav = ({ links }) => {
  const [submenu, setSubmenu] = useState(false);
  const toggleSubmenu = (distance, show) => {
    setSubmenu(true);
    const navInner = document.getElementsByClassName("mobile-nav__inner")[0];
    navInner.style.left = distance;
  };

  const nav = document.getElementsByClassName("mobile-nav")[0];
  const site = document.getElementsByClassName("site-section")[0];
  const body = document.body;
  const menuOff = () => {
    nav.className = "mobile-nav";
    site.className = "site-section";
    site.removeEventListener("touchstart", menuOff, {
      capture: true,
      passive: true,
    });
    setSubmenu(false);
    toggleSubmenu("0");
    setTimeout(() => (body.style.overflow = "scroll"), 200);
  };
  const burgerClick = () => {
    body.style.overflow = "hidden";
    nav.className += " nav-open";
    site.className += " mobile-nav-open";
    site.addEventListener("touchstart", menuOff, {
      capture: true,
      passive: true,
    });
  };
  const burger = document.getElementsByClassName("burger")[0];
  burger.onclick = burgerClick;

  return (
    <div className="mobile-nav__inner">
      <ul className="mobile-nav__list">
        {links.map((item, index) => (
          <NavLink key={index} link={item} toggleSubmenu={toggleSubmenu} />
        ))}
      </ul>
      {submenu && <SubMenu toggleSubmenu={toggleSubmenu} />}
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
