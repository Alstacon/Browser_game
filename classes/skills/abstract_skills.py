from abc import ABC, abstractmethod


class Skill(ABC):
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @abstractmethod
    def skill_effect(self):
        pass

    def _is_stamina_enough(self):
        return self.user.stamina > self.stamina

    def use(self, user, target):
        self.user = user
        self.target = target

        if self._is_stamina_enough:
            return self.skill_effect()
        else:
            return [f"""
            {self.user.name} попытался использовать {self.name}, но у него недостаточно выносливости
            """]
