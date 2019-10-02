from faker import Faker

from .models import TargetGroup as DefaultModel


class TargetGroupFactory():

  @staticmethod
  def create( provider_ids, target_group_model=DefaultModel, instance_count=1):
    root_group_ids = create_root_target_groups(target_group_model, instance_count, provider_ids)
    create_children_target_groups(target_group_model, root_group_ids, provider_ids)

  @staticmethod
  def build(panel_provider_model=DefaultModel):

  @staticmethod
  def _create_root_target_groups(cls, target_group_model, instance_count, all_provider_choices):
    provider_choices_left = set(all_provider_choices)
    root_group_ids = []
    faker = Faker()

    for _ in range(instance_count):
      root_group = target_group_model()
      root_group.name = faker.slug()
      root_group.external_id = faker.random_int()
      root_group.secret_code = faker.uuid4()
      root_group.panel_provider_id = \
        provider_choices_left.pop() if any(provider_choices_left) else random.choice(all_provider_choices)

      root_group.save()
      root_group_ids.append(root_group.id)

    return root_group_ids

  @staticmethod
  def _create_children_target_groups(cls, target_group_model, instance_count, root_group_ids, provider_choices)
    faker = Faker()

    for root_group in target_group_model.objects.filter(id__in=root_group_ids):
      parent = root_group

      for nesting in range(3):
        child_group = target_group_model()
        child_group.name = faker.slug()
        child_group.external_id = faker.random_int()
        child_group.secret_code = faker.uuid4()
        child_group.panel_provider_id = random.choice(provider_choices)
        child_group.parent = parent
        child_group.save()

