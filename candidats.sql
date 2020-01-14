-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Client :  127.0.0.1
-- Généré le :  Mar 14 Janvier 2020 à 09:38
-- Version du serveur :  5.7.14
-- Version de PHP :  5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `bizchallenge`
--

-- --------------------------------------------------------

--
-- Structure de la table `candidats`
--

CREATE TABLE `candidats` (
  `id` int(11) NOT NULL,
  `noms` varchar(255) NOT NULL,
  `solde` varchar(255) NOT NULL,
  `pseudo` varchar(255) NOT NULL,
  `passe` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Contenu de la table `candidats`
--

INSERT INTO `candidats` (`id`, `noms`, `solde`, `pseudo`, `passe`) VALUES
(1, 'denzel', '500', 'denzo525', 'biz25'),
(2, 'goprou', '500', 'goprou214', 'biz65'),
(3, 'inconnu', '500', 'inconnu446', 'biz89'),
(4, 'sminth', '500', 'sminth333', 'biz29'),
(5, 'lolipop', '500', 'lolipop105', 'biz39'),
(6, 'yanic', '500', 'yanic146', 'biz64'),
(7, 'free', '500', 'free752', 'biz83'),
(8, 'GFJH', '500', 'GFJH239', 'biz27'),
(9, 'mike', '500', 'mike580', 'biz99');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `candidats`
--
ALTER TABLE `candidats`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `candidats`
--
ALTER TABLE `candidats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
